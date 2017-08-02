import stormpy
import stormpy.core
import stormpy.pars

import pycarl
import pycarl.cln
import pycarl.core

import stormpy.examples
import stormpy.examples.files

def example_getting_started_05():
    path = stormpy.examples.files.prism_dtmc_die
    prism_program = stormpy.parse_prism_program(path)


    formula_str = "P=? [F s=7 & d=2]"
    properties = stormpy.parse_properties_for_prism_program(formula_str, prism_program)
    model = stormpy.build_model(prism_program, properties)

    for state in model.states:
        for action in state.actions:
            for transition in action.transitions:
                print("from {} with prob {} go to {}".format(state, transition.value(), transition.column))



if __name__ == '__main__':
    example_getting_started_05()