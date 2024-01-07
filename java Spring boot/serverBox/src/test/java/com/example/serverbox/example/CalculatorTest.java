package com.example.serverbox.example;

import org.junit.jupiter.api.Test;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.core.Is.is;

public class CalculatorTest {
    private final Calculator calculator = new Calculator();

    @Test
    void addTest() {
        int actual = calculator.add(1, 2);

        System.out.println("actual: "+actual);
        assertThat(actual, is(3));
    }

    @Test
    void mulTest() {
        int actual = calculator.mul(1, 2);
        int expected = 2;

        System.out.println("메소드 리턴 값 actual: "+actual);
        System.out.println("기대 값 expected: "+expected);
        assertThat(actual, is(expected));
        System.out.println("기대 값 expected: "+is(expected));
    }
}