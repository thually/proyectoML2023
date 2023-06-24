Este repositorio contiene todos los ambientes construidos y referenciados en el proyecto final del curso Machine Learning. Para implementar nuestros ecosistemas usamos como boilerplate el ejemplo usado en el repositorio [gym_examples](https://github.com/Farama-Foundation/gym-examples), decisión que nos facilitaba reutilizar los elementos gráficos de un entorno renderizado mediante pygame, para así dedicarnos principalmente a la implementación de la lógica de cada ambiente.

Los ambientes construidos son:

- PushBoxBaseEnv: Es el ambiente más sencillo y sobre el cuál se basan los demás. Sus características incluyen:

    1. En su estado inicial se dispone un *agente* y una caja o *target* de manera aleatoria.
    2. El agente tiene cuatro posibles acciones, desplazarse hacia arriba, abajo, izquierda y derecha.
    3. Si el agente se encuentra en una posición adyacente al target, y se mueve en la dirección del mismo, entonces lo desplazará (i.e., el agente podrá empujar la caja).
    4. La caja permanece fija en el entorno salvo que el agente la desplaze.
    5. El objetivo del agente es empujar la caja hasta una región definida del ambiente.
    6. La política del agente es binaria y dispersa. Esto quiere decir que el agente obtendrá 0 como recompensa en cada paso que no consigue el objetivo, y obtendrá 1 cuando sí lo logre.

- PushBoxRandEnv: Este ambiente tiene las mismas características que `PushBoxBaseEnv` exceptuando por la característica 4. En este caso el ambiente cambia la caja de forma aleatoria cada cierta cantidad de pasos (definida por el tamaño del ambiente). Adicionalmente añade a la característica 2 una quinta acción: permanecer en la posición actual.

- PushBoxRandEnv2: Comparte las características de `PushBoxRandEnv` pero modifica la política del agente, penalizando cada vez que se mueve o se queda quieto, pero recompensando aún más cada vez que se mueve.
