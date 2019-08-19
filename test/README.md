# Dgen Unit testing

These files have been developed to build and test a dgen document.

## prerequisites

To run the unit test, your machine will need the all the dependencies required by dgen, I suggest you look at dgen's `build.sh` and follow the commands there.

Additionally, you will need to install mock: `pip install mock`.

## How to run

To run the unit tests, execute the following python script: 
```
python test-dgen.py
``` 

The following tests will be performed:

  * Dgen is invoked to generate the `dgen-examples/example-report` using the `default` template
    * Dgen must build without throwing an exception for the test to be successful
  * The test directory is checked for files we expect dgen to create
    * All files in the template's source directory must also be found in the test directory, AND
    * The report's HTML directory must exist, AND
    * The report's *.pdf file must exists, for the test to be successful.
