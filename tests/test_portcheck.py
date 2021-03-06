from PyCat import pycat


class TestBoundaryValue:
    def test_WeakNormal(self):
        assert pycat.portCheck(0)
        assert pycat.portCheck("0")

        assert pycat.portCheck(65535)
        assert pycat.portCheck("65535")

    def test_WeakRobust(self):
        assert not pycat.portCheck(-1)
        assert not pycat.portCheck("-1")

        assert not pycat.portCheck(65536)
        assert not pycat.portCheck("65536")

    def test_StrongNormal(self):
        "Same as weak normal test"
        pass

    def test_StrongRobust(self):
        "Same as weak robust test"
        pass


class TestEquivalenceClass:
    def test_WeakNormal(self):
        assert pycat.portCheck(32768)
        assert pycat.portCheck("32768")

    def test_WeakRobust(self):
        assert not pycat.portCheck(-32768)
        assert not pycat.portCheck("-32768")

        assert not pycat.portCheck(75535)
        assert not pycat.portCheck("75535")

        assert not pycat.portCheck("abc#$%")

    def test_StrongNormal(self):
        "Same as weak normal test"
        pass

    def test_StrongRobust(self):
        "Same as weak robust test"
        pass


class TestEdge:
    def test_WeakNormal(self):
        assert pycat.portCheck(1)
        assert pycat.portCheck("1")

        assert pycat.portCheck(65534)
        assert pycat.portCheck("65534")

    def test_WeakRobust(self):
        assert not pycat.portCheck(-2)
        assert not pycat.portCheck("-2")

        assert not pycat.portCheck(65537)
        assert not pycat.portCheck("65537")

        assert not pycat.portCheck("")
        assert not pycat.portCheck("@@@@@")

    def test_StrongNormal(self):
        "Same as weak normal test"
        pass

    def test_StrongRobust(self):
        "Same as weak robust test"
        pass
