import re


# Define token types
class TokenType:
    INT = "INT"
    IDENTIFIER = "IDENTIFIER"
    NUMBER = "NUMBER"
    ASSIGN = "ASSIGN"
    PLUS = "PLUS"
    MINUS = "MINUS"
    IF = "IF"
    EQUAL = "EQUAL"
    LBRACE = "LBRACE"
    RBRACE = "RBRACE"
    SEMICOLON = "SEMICOLON"
    UNKNOWN = "UNKNOWN"
    EOF = "EOF"


# Token structure
class Token:
    def __init__(self, type, text):
        self.type = type
        self.text = text

    def __repr__(self):
        return f"Token({self.type}, '{self.text}')"


# Lexer class
class Lexer:
    def __init__(self, input_text):
        self.input = input_text
        self.position = 0
        self.length = len(input_text)

    def get_next_char(self):
        if self.position < self.length:
            char = self.input[self.position]
            self.position += 1
            return char
        return None

    def peek_next_char(self):
        if self.position < self.length:
            return self.input[self.position]
        return None

    def get_next_token(self):
        while self.position < self.length:
            current_char = self.get_next_char()

            # Skip whitespace
            if current_char.isspace():
                continue

            # Keywords and Identifiers
            if current_char.isalpha():
                identifier = current_char
                while (next_char := self.peek_next_char()) and next_char.isalnum():
                    identifier += self.get_next_char()
                if identifier == "int":
                    return Token(TokenType.INT, identifier)
                elif identifier == "if":
                    return Token(TokenType.IF, identifier)
                return Token(TokenType.IDENTIFIER, identifier)

            # Numbers
            if current_char.isdigit():
                number = current_char
                while (next_char := self.peek_next_char()) and next_char.isdigit():
                    number += self.get_next_char()
                return Token(TokenType.NUMBER, number)

            # Single-character tokens
            if current_char == "=":
                return Token(TokenType.ASSIGN, "=")
            if current_char == "+":
                return Token(TokenType.PLUS, "+")
            if current_char == "-":
                return Token(TokenType.MINUS, "-")
            if current_char == "{":
                return Token(TokenType.LBRACE, "{")
            if current_char == "}":
                return Token(TokenType.RBRACE, "}")
            if current_char == ";":
                return Token(TokenType.SEMICOLON, ";")

            # If character is unknown
            return Token(TokenType.UNKNOWN, current_char)

        return Token(TokenType.EOF, "")


# Main for testing the lexer
if __name__ == "__main__":
    # Example input
    input_code = """
    int x = 10;
    if (x == 10) {
        x = x + 1;
    }
    """

    # Initialize the lexer
    lexer = Lexer(input_code)
    token = lexer.get_next_token()

    # Print all tokens
    while token.type != TokenType.EOF:
        print(token)
        token = lexer.get_next_token()
