# Tests for Creddie App

These tests are located outside of the application because we do not ship Creddie with tests inside.  

However, these tests are primarily unit tests. While the boundaries between unit, integration, etc. often get blurred, these tests will cover both the functionality of internal functions, as well as test some endpoints.  

You need to be careful when writing tests. It can be tempting to use variables defined in the package to make testing faster, but that can lead to the tests not meaning much. For example, if an API route returns a string, if you make that string a global variable, you can import it and use it in the test. But, what you lose is that now your test and behavior are coupled, so the test doesn't assert the output as being something specific, it now only tells you that the variable wasn't corrupted somewhere inbetween.
