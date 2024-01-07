package com.example.firstproject.config;

import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.encryption.pbe.config.SimpleStringPBEConfig;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.data.domain.Sort;


@SpringBootTest(classes = JasyptConfig.class)
public class JasyptConfigTest {
    private static final String password = "password"; // 키 암호화에 사용할 암호
    private static final String algorithm = "PBEWithMD5AndDES"; // 키 암호화 알고리즘

    @Test
    void encryptTest() {
        String id = "root";
        String password = "0000";

        System.out.println("==== 암호화 ====");
        id = encryptKey("root");
        password = encryptKey("0000");
        System.out.println("id : "+id);
        System.out.println("password : "+password);

        System.out.println("\n\n==== 복호화 ====");
        id = decryptKey(id);
        password = decryptKey(password);
        System.out.println("id : "+id);
        System.out.println("password : "+password);
    }

    // 암호화
    private String encryptKey(String key) {
        StandardPBEStringEncryptor encryptor = new StandardPBEStringEncryptor();
        SimpleStringPBEConfig config = new SimpleStringPBEConfig();
        config.setPassword(password); // 암호 키 설정
        config.setAlgorithm(algorithm); // 해시 알고리즘
        encryptor.setConfig(config);

        return encryptor.encrypt(key);
    }

    // 복호화
    private String decryptKey(String key) {
        StandardPBEStringEncryptor encryptor = new StandardPBEStringEncryptor();
        SimpleStringPBEConfig config = new SimpleStringPBEConfig();
        config.setPassword(password); // 암호 키 설정
        config.setAlgorithm(algorithm); // 해시 알고리즘
        encryptor.setConfig(config);

        return encryptor.decrypt(key);
    }
}