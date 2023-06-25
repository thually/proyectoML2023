Este repositorio contiene todos los ambientes construidos y referenciados en el proyecto final del curso Machine Learning. Para implementar nuestros ecosistemas usamos como boilerplate el ejemplo usado en el repositorio [gym_examples](https://github.com/Farama-Foundation/gym-examples), decisión que nos facilitaba reutilizar los elementos gráficos de un entorno renderizado mediante pygame, para así dedicarnos principalmente a la implementación de la lógica de cada ambiente.

Los ambientes construidos son:

- PushBox: Es el ambiente más sencillo y sobre el cuál se basan los demás. Sus características incluyen:

    1. En su estado inicial se dispone un *agente* y una caja o *target* de manera aleatoria.
    2. El agente tiene cuatro posibles acciones, desplazarse hacia arriba, abajo, izquierda y derecha.
    3. Si el agente se encuentra en una posición adyacente al target, y se mueve en la dirección del mismo, entonces lo desplazará (i.e., el agente podrá empujar la caja).
    4. La caja permanece fija en el entorno salvo que el agente la desplaze.
    5. El objetivo del agente es empujar la caja hasta una región definida del ambiente.
    6. La política del agente es binaria y dispersa. Esto quiere decir que el agente obtendrá 0 como recompensa en cada paso que no consigue el objetivo, y obtendrá 1 cuando sí lo logre.

- PushBoxRand: Este ambiente tiene las mismas características que `PushBoxBaseEnv` exceptuando por la característica 4. En este caso el ambiente cambia la caja de forma aleatoria cada cierta cantidad de pasos (definida por el tamaño del ambiente). Adicionalmente añade a la característica 2 una quinta acción: permanecer en la posición actual.

- PushBoxRand2: Comparte las características de `PushBoxRandEnv` pero modifica la política del agente, penalizando cada vez que se mueve o se queda quieto, pero recompensando aún más cada vez que logre el objetivo.


---

# Changelog

## PushBox

1. Actualización en las importaciones, los módulos y los requerimientos del módulo: https://github.com/thually/proyectoML2023/commit/03437e009c3d394f4a79dea00dace97ee1f4d821

2. Cambios gráficos: https://github.com/thually/proyectoML2023/commit/224e7782bf74c35526ae7f7b8bc816a3e0370ae5, https://github.com/thually/proyectoML2023/commit/58b5b5a1a16844f157859644f6b0902f2a035dc1, https://github.com/thually/proyectoML2023/commit/2fee43ff3553375e5362721e950916c262c39c47, https://github.com/thually/proyectoML2023/commit/926fb903516f7e3e2e7231539c08c498f682e4c4.

3. Modificación en la lógica del método reset: https://github.com/thually/proyectoML2023/commit/a0220b6a4512d80afea37797745cfd0005e9ad64, https://github.com/thually/proyectoML2023/commit/536644435dc3bb03812c94c30eab79aca4411a3e

4. Modificación en la lógica del método step: https://github.com/thually/proyectoML2023/commit/509e4257795fd9256db59a5150a6aa915ee71ce9, https://github.com/thually/proyectoML2023/commit/536644435dc3bb03812c94c30eab79aca4411a3e



