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

A continuación dejamos el registro de cambios que se realizó sobre cada entorno del proyecto, a partir del fork original

## PushBox (Entorno base)

1. Actualización en las importaciones, los módulos y los requerimientos del módulo: thually/proyectoML2023@03437e0

2. Cambios gráficos: 224e778, 58b5b5a, 2fee43f, 926fb90.

3. Modificación en la lógica del método reset: a0220b6, 5366444

4. Modificación en la lógica del método step: 509e425, 5366444



