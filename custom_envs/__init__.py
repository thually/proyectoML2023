from gymnasium.envs.registration import register

register(
     id="custom_envs/PushBoxBase",
     entry_point="custom_envs.envs:PushBoxBaseEnv",
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
