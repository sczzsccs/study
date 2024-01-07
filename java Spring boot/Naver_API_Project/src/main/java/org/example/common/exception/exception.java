package org.example.common.exception;

import org.example.common.Constants;
import org.springframework.http.HttpStatus;

public class exception extends Exception {
    private static final long serialVersionUID = 4663380430591151694L;
//    private Constants.ExceptionClass exceptionClass;
    private HttpStatus httpStatus;

//    public exception(Constants.ExceptionClass exceptionClass, HttpStatus httpStatus, String message) {
//        super(exceptionClass.toString() + message);
//        this.exceptionClass = exceptionClass;
//        this.httpStatus = httpStatus;
//    }
}
