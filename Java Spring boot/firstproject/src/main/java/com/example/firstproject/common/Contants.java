package com.example.firstproject.common;

public class Contants {
    public enum ExceptionClass {
        PRODUCT("Product"), ORDER("Order"), PROVIDER("Provider");
        private String exceptionclass;
        ExceptionClass(String exceptionclass) {
            this.exceptionclass = exceptionclass;
        }
        public String getExceptionclass() {
            return exceptionclass;
        }

        @Override
        public String toString() {
            return getExceptionclass()+"Exception. ";
        }
    }
}
