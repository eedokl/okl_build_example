from calculator.core import Calculator

def test_class_instantiate_ok():
    calculator = Calculator()
    assert calculator is not None

def test_add_works():
    # Arrange
    calculator = Calculator()
    operator1, operator2, expected = 3,7,10
    # Act
    result = calculator.Add(operator1, operator2)
    # Assert
    assert result == expected

def test_substract_works():
    # Arrange
    calculator = Calculator()
    operator1, operator2, expected = 8,3,5
    # Act
    result = calculator.Substract(operator1, operator2)
    # Assert
    assert result == expected

def test_multiply_works():
    # Arrange
    calculator = Calculator()
    operator1, operator2, expected = 5,5,25
    # Act
    result = calculator.Multiply(operator1, operator2)
    # Assert
    assert result == expected

def test_divide_works():
    # Arrange
    calculator = Calculator()
    operator1, operator2, expected = 40,8,5
    # Act
    result = calculator.Divide(operator1, operator2)
    # Assert
    assert result == expected