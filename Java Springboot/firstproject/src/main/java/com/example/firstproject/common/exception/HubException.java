package com.example.firstproject.common.exception;

import com.example.firstproject.common.Contants;
import lombok.Getter;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;

import java.io.Serial;

@Getter
@Slf4j
public class HubException extends Exception {
    @Serial
    private static final long serialVersionUID = 4663380430591151694L;
    private final Contants.ExceptionClass exceptionClass;
    private final HttpStatus httpStatus;

    public HubException(Contants.ExceptionClass exceptionClass, HttpStatus httpStatus, String message) {
        super(exceptionClass.toString()+message);
//        log.info(exceptionClass.toString()+message);
        this.exceptionClass = exceptionClass;
        this.httpStatus = httpStatus;
    }

    public int getHttpStatusCode() {
        return httpStatus.value();
    }
    public String getHttpStatusType() {
        return httpStatus.getReasonPhrase();
    }
}