package org.example.data.entity;

import jakarta.persistence.*;
import lombok.*;

@Entity
@Getter
@Setter
@ToString
@NoArgsConstructor
@AllArgsConstructor
@Builder
@Table(name = "short_url")
public class ShortUrlEntity extends BaseEntity {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long iD;
    @Column(nullable = false, unique = true)
    private String hash;
    @Column(nullable = false, unique = true)
    private String orgUrl;
    @Column(nullable = false, unique = true)
    private String url;

}