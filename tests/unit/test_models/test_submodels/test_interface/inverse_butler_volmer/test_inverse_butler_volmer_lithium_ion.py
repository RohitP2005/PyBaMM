#
# Test lithium-ion inverse butler volmer submodel
#

import pybamm
import tests
import unittest


class TestLithiumIon(unittest.TestCase):
    def test_public_functions(self):
        param = pybamm.standard_parameters_lithium_ion

        a = pybamm.Scalar(0)
        variables = {
            "Current collector current density": a,
            "Negative electrode interfacial current density": a,
            "Negative electrode open circuit potential": a,
            "Negative electrolyte concentration": a,
            "Negative particle surface concentration": a,
        }
        submodel = pybamm.interface.inverse_butler_volmer.LithiumIon(param, "Negative")
        std_tests = tests.StandardSubModelTests(submodel, variables)

        std_tests.test_all()

        variables = {
            "Current collector current density": a,
            "Negative electrode interfacial current density": a,
            "Negative electrode exchange current density": a,
            "Positive electrode open circuit potential": a,
            "Positive electrolyte concentration": a,
            "Positive particle surface concentration": a,
        }
        submodel = pybamm.interface.inverse_butler_volmer.LithiumIon(param, "Positive")
        std_tests = tests.StandardSubModelTests(submodel, variables)
        std_tests.test_all()


if __name__ == "__main__":
    print("Add -v for more debug output")
    import sys

    if "-v" in sys.argv:
        debug = True
    unittest.main()
