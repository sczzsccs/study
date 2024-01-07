package org.example.entity;

import jakarta.persistence.*;
import lombok.*;
import org.springframework.data.annotation.CreatedDate;
import org.springframework.data.jpa.domain.support.AuditingEntityListener;
import java.time.LocalDateTime;

@Getter
@Setter
@Data
@Entity
@Builder
@NoArgsConstructor
@AllArgsConstructor
@Table(name = "product")
@EntityListeners(AuditingEntityListener.class)
public class ProductEntity {
    @Id
    private String ProductName;
    private Integer cost;
    @CreatedDate
    private LocalDateTime makeDate;
    private String company;
    private Integer amount;

    public ProductEntity(
            String Name,
            Integer cost,
            String company,
            Integer amount) {
        this.ProductName = Name;
        this.cost = cost;
        this.company = company;
        this.amount = amount;
    }
}
