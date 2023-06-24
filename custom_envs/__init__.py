from gymnasium.envs.registration import register

register(
     id="custom_envs/PushBox",
     entry_point="custom_envs.envs:PushBoxEnv",
     max_episode_steps=300,
)

register(
     id="custom_envs/PushBoxRandom",
     entry_point="custom_envs.envs:PushBoxRandEnv",
     max_episode_steps=300,
)

register(
     id="custom_envs/PushBoxRandom2",
     entry_point="custom_envs.envs:PushBoxRand2Env",
     max_episode_steps=300,
)
