class NodoAVL:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class ArbolAVL:
    def __init__(self):
        self.root = None

    def insertar(self, key, value):
        self.root = self._insertar(self.root, key, value)

    def _insertar(self, nodo, key, value):
        if not nodo:
            return NodoAVL(key, value)
        elif key < nodo.key:
            nodo.left = self._insertar(nodo.left, key, value)
        else:
            nodo.right = self._insertar(nodo.right, key, value)

        nodo.height = 1 + max(self._get_height(nodo.left), self._get_height(nodo.right))

        balance = self._get_balance(nodo)

        if balance > 1 and key < nodo.left.key:
            return self._rotar_derecha(nodo)
        if balance < -1 and key > nodo.right.key:
            return self._rotar_izquierda(nodo)
        if balance > 1 and key > nodo.left.key:
            nodo.left = self._rotar_izquierda(nodo.left)
            return self._rotar_derecha(nodo)
        if balance < -1 and key < nodo.right.key:
            nodo.right = self._rotar_derecha(nodo.right)
            return self._rotar_izquierda(nodo)

        return nodo

    def _rotar_izquierda(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _rotar_derecha(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _get_height(self, nodo):
        if not nodo:
            return 0
        return nodo.height

    def _get_balance(self, nodo):
        if not nodo:
            return 0
        return self._get_height(nodo.left) - self._get_height(nodo.right)

    def preorden(self, nodo):
        if not nodo:
            return
        print(f"{nodo.key}: {nodo.value}")
        self.preorden(nodo.left)
        self.preorden(nodo.right)