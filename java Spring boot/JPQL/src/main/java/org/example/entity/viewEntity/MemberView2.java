package org.example.entity.viewEntity;


import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.*;
import org.hibernate.annotations.Subselect;
import org.springframework.data.annotation.Immutable;

@Getter
@Setter
@Data
@Entity
@AllArgsConstructor
@NoArgsConstructor
@Immutable // view table 수정불가
@Table(name = "member_view2")
/* Sql에서 생성된 View 매핑을 통해 조회 */
public class MemberView2 {
    @Id
    private String memberId;
    private String memberName;
    private String memberAddr;
}
