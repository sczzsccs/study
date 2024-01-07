package org.example.entity.viewEntity;

import jakarta.persistence.*;
import lombok.*;
import org.hibernate.annotations.Subselect;
import org.springframework.data.annotation.Immutable;

@Getter
@Setter
@Data
@Entity
@AllArgsConstructor
@NoArgsConstructor
//@Immutable // view table 수정불가
@Subselect("""
    select * from member
""")
/* JPA로 생성된 ViewEntity Sql로 조회불가 */
public class MemberView {
    @Id
    private String memberId;
    @Column(name = "member_name")
    private String memberName;
    private String memberAddr;
}