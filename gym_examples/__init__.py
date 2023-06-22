from gymnasium.envs.registration import register

register(
     id="gym_examples/GridWorld-v0",
     entry_point="gym_examples.envs:GridWorldEnv",
     max_episode_steps=300,
)

register(
     id="gym_examples/GridWorldRandom-v0",
     entry_point="gym_examples.envs:GridWorldRandEnv",
     max_episode_steps=300,
)

register(
     id="gym_examples/GridWorldRandom-v1",
     entry_point="gym_examples.envs:GridWorldRandEnv_v1",
     max_episode_steps=300,
)