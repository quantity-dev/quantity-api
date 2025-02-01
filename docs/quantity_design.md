# Background

There are a number of libraries which provide unit support in Python, such as `astropy.units`, `pint` and `unyt`. Although these libraries provide classes with the same core functionality, attributes and methods are named differently, which makes it difficult to write code compatible with multiple libraries.

This has led to ecosystems centred around each unit library, as libraries that depend on one unit library are incompatible with those written with other unit libraries. This also prevents libraries that could support units from doing so, as maintainers may not wish to pick one library over another or maintain code for multiple libraries.

The maintainers of unit libraries have recognized these issues and issues and have come together to create a quantity/unit API that would allow downstream libraries to support all unit libraries adhering to the API.


# Design Principles

## Classes

The API shall standardize the classes, methods, attributes and errors commonly used across existing unit libraries. Existing libraries use classes to provide unit support.

## Universality

Standardized classes should reflect common usage of existing libraries. Functionality that exists (or desired) in multiple libraries should be standardised.

## Extensible

Libraries may implement methods and attributes not covered by the API.

## Protocols

The standardized API shall consist of PEP 544 Protocols that define naming and functionality of classes and allows for standardized, static type-checking.

## Naming

The API is intended to allow for use with the array API, so names of methods and attributes should not conflict with array methods/attributes and should be unambiguous without the context of providing unit support.