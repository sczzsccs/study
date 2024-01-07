package com.example.firstproject.config;

import com.zaxxer.hikari.HikariConfig;
import com.zaxxer.hikari.HikariDataSource;
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.encryption.pbe.config.SimpleStringPBEConfig;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import javax.sql.DataSource;

@Configuration
public class DatabaseConfig {
    private Logger LOGGER = LoggerFactory.getLogger(DatabaseConfig.class);

    @Value("${spring.datasource.username}")
    private String encryptedUsername;
    @Value("${spring.datasource.password}")
    private String encryptedPassword;

    @Bean
    public DataSource dataSource() {
        try {
            // 기존 코드...
            final String key = "password"; // 암호
            final String hash = "PBEWithMD5AndDES"; // 해시 암호

            LOGGER.info("\n\n===== 암호화 된 키 =====");
            LOGGER.info("properties Id: "+encryptedUsername);
            LOGGER.info("properties Password: "+encryptedUsername);

            // Jasypt를 사용하여 복호화
            StandardPBEStringEncryptor encryptor = new StandardPBEStringEncryptor();
            SimpleStringPBEConfig config = new SimpleStringPBEConfig();
            config.setPassword(key); // 암호 키 설정
            config.setAlgorithm(hash); // 해시 알고리즘
            encryptor.setConfig(config);

            String decryptedUsername = encryptor.decrypt(encryptedUsername);
            String decryptedPassword = encryptor.decrypt(encryptedPassword);

            LOGGER.info("\n\n===== 복호화 된 키 =====");
            LOGGER.info("properties Id: "+decryptedUsername);
            LOGGER.info("properties Password: "+decryptedPassword);

            // 이제 decryptedUsername와 decryptedPassword를 사용하여 DataSource를 구성하고 반환
            HikariConfig Hconfig = new HikariConfig();
            Hconfig.setJdbcUrl("jdbc:mysql://localhost:3306/first_db?&characterEncoding=UTF-8");
            Hconfig.setUsername(decryptedUsername);
            Hconfig.setPassword(decryptedPassword);

            return new HikariDataSource(Hconfig);
        } catch (Exception e) {
            LOGGER.error("Error creating data source", e);
            throw new RuntimeException("Error creating data source", e); // 예외를 다시 던져서 스프링이 예외를 감지할 수 있도록 합시다.
        }
    }
}