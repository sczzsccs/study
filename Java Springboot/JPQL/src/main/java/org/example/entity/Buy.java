package org.example.entity;

import jakarta.persistence.*;
import lombok.*;
@Data
@Entity
@AllArgsConstructor
@NoArgsConstructor
@Table(name = "buy")
public class Buy {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    Integer prodNum;
    String prodId;
    String prodname;
    String prodgroup;
    Integer price;
    Integer amount;
}