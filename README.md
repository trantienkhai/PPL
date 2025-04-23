# MiniGo Compiler – PPL Course Project
This project is developed as part of the *Principles of Programming Languages (CO3005)* course at Ho Chi Minh City University of Technology – VNU-HCM. The compiler targets **MiniGo**, a simplified subset of the Go programming language, and is implemented in **Python** using **ANTLR 4.9.2**.
### Assignment 1: Lexer & Parser
- Implemented the lexer and parser using **ANTLR** based on the official MiniGo grammar specification.
- Developed 100 test cases for both lexical and syntactic correctness.
- **Score:** Lexer: 100/100, Parser: 82/100

### Assignment 2: AST Generation
- Converted parse trees into Abstract Syntax Trees (AST) using the **Visitor Pattern**.
- Handled a wide range of MiniGo syntax constructs including literals, expressions, declarations, functions, and methods.
- **Score:** 93/100

### Assignment 3: Static Checker
- Implemented a semantic checker for MiniGo, validating:
  - Redeclarations
  - Undeclared identifiers
  - Type mismatches
- Built using Python OOP and structured error handling.

## Technologies & Tools
- Python 3.12
- ANTLR 4.9.2
- Git for version control
- Unit testing with custom test suites
