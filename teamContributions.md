**Xavier: API Interaction**

1.  OpenAI API Setup

    -   Create an OpenAI account and obtain an API key.
    -   Set up the API key as an environment variable in the development environment.
    -   Install necessary Python libraries for making HTTP requests (such as `requests`).
2.  Integration with OpenAI API

    -   Develop functionality to generate prompts based on extracted code information and send these prompts to the OpenAI API.
    -   Handle API responses and extract generated text.
    -   Implement error handling for API requests.
3.  README Generation

    -   Develop functionality to generate a prompt for the README file based on the overall code structure and functionality.
    -   Send the prompt to the OpenAI API and extract the generated text.
    -   Write the generated text to a README file.

**Elias: File Reading/Writing**

1.  Project Setup

    -   Set up a new Python project in your development environment of choice.
    -   Create a GitHub repository for the project.
    -   Set up a Python virtual environment for the project.
2.  Code Parsing

    -   Develop functionality to read and parse code files in different languages.
    -   Identify sections of the code that need documentation/comments.
    -   Develop functionality to extract function signatures, class definitions, and other relevant information.
3.  Code Modification

    -   Develop functionality to insert the generated text as comments/documentation in the appropriate places in the code.
    -   Make sure that the inserted comments match the formatting and style requirements of the respective language.
4.  User Interface

    -   Develop a CLI (Command Line Interface) for users to input the file name.
    -   Handle any possible errors in user input and provide useful feedback.

**Mohammed: Testing and Databases**

1.  Testing

    -   Develop unit tests for the different components of your project.
    -   Ensure that the generated documentation/comments make sense and add value to the code.
2.  GitHub Automation

    -   Set up GitHub Actions for automated testing and style checking.
3.  Project Review and Refinement

    -   Review the project functionality and make necessary adjustments and improvements.
    -   Check the project against the PEP8 style guide and make necessary corrections.
4.  Documentation

    -   Write comprehensive documentation for the project, including how to set up, use, and contribute to the project.
5. Database
    - Brainstorm how databases can be used to store text we are sending and receiving from API. Implement this in the codebase to allow for access
