package org.example.data.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;
import org.springframework.data.annotation.CreatedDate;
import org.springframework.data.annotation.LastModifiedDate;
import org.springframework.data.jpa.domain.support.AuditingEntityListener;

import java.time.*;

@Getter
@Setter
@MappedSuperclass
@EntityListeners(AuditingEntityListener.class)
public class BaseEntity {
    @CreatedDate @Column(updatable = false)
    private LocalDateTime createdAt;
    @LastModifiedDate
    private LocalDateTime updatedAt;

//    @PrePersist
//    private void prePresist() {
//        createdAt = ZonedDateTime.now();
//        updatedAt = ZonedDateTime.now();
//    }
//    @PreUpdate
//    private void preUpdate() {
//        updatedAt = ZonedDateTime.now();
//    }
}