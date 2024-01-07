package org.example.entity;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.*;

import java.sql.Date;
import java.time.LocalDate;

@Data
@Entity
@AllArgsConstructor
@NoArgsConstructor
@Table(name = "girl_member")
public class GirlMember {
    @Id
    String memId;
    String name;
    Integer memNum;
    String addr;
    String PhoneNum1;
    String PhoneNum2;
    Integer height;
    LocalDate debutDate;
}