#!/bin/bash
nosetests visa/test/cybersource/test_cybersource_keygeneration.py -s
nosetests visa/test/helloworld/test_helloworld_payment.py -s
