package org.example.entity;

import jakarta.persistence.*;
import lombok.*;


@Getter
@Setter
@Data
@Entity
@AllArgsConstructor
@NoArgsConstructor
@Table(name = "member",
        indexes = {@Index(name = "member_idx", columnList = "member_name")})
public class MemberEntity {
    @Id
    private String memberId;
    @Column(name = "member_name")
    private String memberName;
    private String memberAddr;
}