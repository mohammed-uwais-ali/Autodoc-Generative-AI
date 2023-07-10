import unittest
from autodoc import AutoDoc

class testingAutoDoc(unittest.TestCase):
    def setUp(self):
        self.autoDoc = AutoDoc()
        
    def tearDown(self):
        pass

    def testReadFile(self):
        file_name = "fileForTestingReading.py"
        actualText = self.autoDoc.readFile(file_name)
        expectedText = "\ndef square(n):\n\n    return n * n\n\n\n\nnumber = 55\n\nresult = square(number)\n"
                        
        self.assertEqual(actualText, expectedText)

    def testWriteFile(self):
        file_name = "fileForTestingWriting.py"
        responseText = "\ndef square(n):\n  return n * n\nnumber = 55\nresult = square(number)\n"
        #using readFile method to visit file and then check writeFile method's accuracy
        self.autoDoc.writeFile(responseText, file_name)
        returnedText = self. autoDoc.readFile(file_name)
        #readFile will add new lines to that same code
        expectedText = "\n\n\ndef square(n):\n\n  return n * n\n\nnumber = 55\n\nresult = square(number)\n\n"
        self.assertEqual(returnedText, expectedText)
    #test will ensure that each line of the return value is equal
    # def testwriteFile(self):
        # return a-b

    def testCallapi(self):
        inputText = "\ndef square(n):\n  return n * n\nnumber = 55\nresult = square(number)\n"
        outputTextFromAPI = self.autoDoc.call_api(inputText)
        self.assertGreater(len(outputTextFromAPI), len(inputText))

if __name__ == "__main__":
    unittest.main()
