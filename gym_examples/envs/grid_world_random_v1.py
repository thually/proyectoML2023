import numpy as np
import pygame

import gymnasium as gym
from gymnasium import spaces


class GridWorldRandEnv_v1(gym.Env):
    metadata = {"render_modes": ["human", "rgb_array"], "render_fps": 4}

    def __init__(self, render_mode=None, size=5, step_limit=None):
        self.size = size  # The size of the square grid
        # steps before target changes position
        if step_limit is None: self.step_limit = size
        else: self.step_limit = step_limit
        self.window_size = 512  # The size of the PyGame window

        # Observations are dictionaries with the agent's and the target's location.
        # Each location is encoded as an element of {0, ..., `size`-1}^2, i.e. MultiDiscrete([size, size]).
        self.observation_space = spaces.Dict(
            {
                "agent": spaces.Box(0, size - 1, shape=(2,), dtype=int),
                "target": spaces.Box(0, size - 1, shape=(2,), dtype=int),
            }
        )

        # We have 4 actions, corresponding to "right", "up", "left", "down", "right", "stay"
        self.action_space = spaces.Discrete(5)

        """
        The following dictionary maps abstract actions from `self.action_space` to 
        the direction we will walk in if that action is taken.
        I.e. 0 corresponds to "right", 1 to "up" etc.
        """
        self._action_to_direction = {
            0: np.array([1, 0]),
            1: np.array([0, 1]),
            2: np.array([-1, 0]),
            3: np.array([0, -1]),
            4: np.array([0, 0]),
        }

        assert render_mode is None or render_mode in self.metadata["render_modes"]
        self.render_mode = render_mode

        """
        If human-rendering is used, `self.window` will be a reference
        to the window that we draw to. `self.clock` will be a clock that is used
        to ensure that the environment is rendered at the correct framerate in
        human-mode. They will remain `None` until human-mode is used for the
        first time.
        """
        self.window = None
        self.clock = None

    def _get_obs(self):
        return {"agent": self._agent_location, "target": self._target_location}

    def _get_info(self):
        return {
            "distance": np.linalg.norm(
                self._agent_location - self._target_location, ord=1
            )
        }

    def reset(self, seed=None, options=None):
        # We need the following line to seed self.np_random
        super().reset(seed=seed)

        self.step_limit = self.size # steps before target changes position

        # Choose the agent's location uniformly at random
        self._agent_location = self.np_random.integers(0, self.size, size=2, dtype=int)

        # We will sample the target's location randomly until it does not coincide with the agent's location
        # or until it is not on the left or right border of the grid
        self._target_location = self._agent_location
        while np.array_equal(self._target_location, self._agent_location) or self._target_location[0] in [0, self.size-1]:
            self._target_location = self.np_random.integers(
                0, self.size, size=2, dtype=int
            )

        observation = self._get_obs()
        info = self._get_info()

        if self.render_mode == "human":
            self._render_frame()

        return observation, info

    def step(self, action):
        # An episode is done iff the agent has reached the target
        terminated = self._target_location[0] == self.size - 1

        # if self.step_limit == 0 change target location
        if self.step_limit == 0:
            self.step_limit = self.size
            self._target_location = self._agent_location
            while np.array_equal(self._target_location, self._agent_location) or self._target_location[0] in [0, self.size-1]:
                self._target_location = self.np_random.integers(
                    0, self.size, size=2, dtype=int
            )
        
        # Map the action (element of {0,1,2,3,4}) to the direction we walk in
        direction = self._action_to_direction[action]
        # We use `np.clip` to make sure we don't leave the grid
        if np.array_equal(self._agent_location + direction, self._target_location):
            # If the agent would walk into the target, we push the target in the same direction
            # and move the agent, if possible.
            # If the target would leave the grid, we don't the target nor the agent.

            clipped_target_location = np.clip(
                self._target_location + direction, 0, self.size - 1
            )

            if not np.array_equal(self._target_location, clipped_target_location):


                self._target_location = clipped_target_location
                self._agent_location = np.clip(
                    self._agent_location + direction, 0, self.size - 1
                )

        else:
            # Otherwise, we move the agent
            self._agent_location = np.clip(
                self._agent_location + direction, 0, self.size - 1
            )

        # reduce step limit
        self.step_limit -= 1


        # An episode is truncated iff the agent has reached the left border of the grid
        truncated = self._target_location[0] == 0

        # A more complicated reward function
        if terminated:
            # If target is in goal, we give a reward of 10
            reward = 30
        elif action == 4:
            # If the agent stays, we give a reward of -1
            reward = -1
        else:
            # if the agent moves, we give a reward of -2
            reward = -2

        observation = self._get_obs()
        info = self._get_info()

        if self.render_mode == "human":
            self._render_frame()

        return observation, reward, terminated, truncated, info

    def render(self):
        if self.render_mode == "rgb_array":
            return self._render_frame()

    def _render_frame(self):
        if self.window is None and self.render_mode == "human":
            pygame.init()
            pygame.display.init()
            self.window = pygame.display.set_mode((self.window_size, self.window_size))
        if self.clock is None and self.render_mode == "human":
            self.clock = pygame.time.Clock()

        canvas = pygame.Surface((self.window_size, self.window_size))
        canvas.fill((255, 255, 255))
        pix_square_size = (
            self.window_size / self.size
        )  # The size of a single grid square in pixels

        # First, we draw the orange goal zone
        pygame.draw.rect(
            canvas,
            (255, 165, 0),
            pygame.Rect(
                (pix_square_size * (self.size-1), 0),
                (pix_square_size, pix_square_size*self.size),
            ),
        )

        # we draw the target
        pygame.draw.rect(
            canvas,
            (238, 130, 238),
            pygame.Rect(
                pix_square_size * self._target_location,
                (pix_square_size, pix_square_size),
            ),
        )
        # Now we draw the agent
        pygame.draw.circle(
            canvas,
            (64, 224, 208),
            (self._agent_location + 0.5) * pix_square_size,
            pix_square_size / 3,
        )

        # Finally, add some gridlines
        pygame.draw.line(
            canvas,
            0,
            (0, 0),
            (self.window_size, 0),
            width=3,
        )
        pygame.draw.line(
            canvas,
            0,
            (0, pix_square_size * self.size),
            (self.window_size, pix_square_size * self.size),
            width=3,
        )
        for x in range(self.size + 1):
            pygame.draw.line(
                canvas,
                0,
                (0, pix_square_size * x),
                (self.window_size - pix_square_size, pix_square_size * x),
                width=3,
            )
            pygame.draw.line(
                canvas,
                0,
                (pix_square_size * x, 0),
                (pix_square_size * x, self.window_size),
                width=3,
            )

        if self.render_mode == "human":
            # The following line copies our drawings from `canvas` to the visible window
            self.window.blit(canvas, canvas.get_rect())
            pygame.event.pump()
            pygame.display.update()

            # We need to ensure that human-rendering occurs at the predefined framerate.
            # The following line will automatically add a delay to keep the framerate stable.
            self.clock.tick(self.metadata["render_fps"])
        else:  # rgb_array
            return np.transpose(
                np.array(pygame.surfarray.pixels3d(canvas)), axes=(1, 0, 2)
            )

    def close(self):
        if self.window is not None:
            pygame.display.quit()
            pygame.quit()
