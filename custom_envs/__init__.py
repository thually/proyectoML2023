from gymnasium.envs.registration import register

register(
     id="custom_envs/PushBox",
     entry_point="custom_envs.envs:PushBoxEnv",
     max_episode_steps=300,
)

register(
     id="custom_envs/PushBoxRand",
     entry_point="custom_envs.envs:PushBoxRandEnv",
     max_episode_steps=300,
)

register(
     id="custom_envs/PushBoxRandPol1",
     entry_point="custom_envs.envs:PushBoxRandPol1Env",
     max_episode_steps=300,
)

register(
     id="custom_envs/PushBoxRandPol2",
     entry_point="custom_envs.envs:PushBoxRandPol2Env",
     max_episode_steps=300,
)
