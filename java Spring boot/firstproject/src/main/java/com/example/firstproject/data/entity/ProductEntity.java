package com.example.firstproject.data.entity;

import com.example.firstproject.data.dto.ProductDTO;
import com.example.firstproject.data.entity.listener.CustomListener;
import jakarta.persistence.*;
import lombok.*;

@Entity
@Getter
@Setter
@ToString
@NoArgsConstructor
@AllArgsConstructor
@Builder
@Table(name = "product_table")
//@EntityListeners(CustomListener.class)
public class ProductEntity extends BaseEntity {
    @Id
    private String productId; // PK(기본 키)
    private String productName;
    private Integer productPrice;
    private Integer productStock;


    /*
    @Column
    String sellerId;

    @Column
    String sellerPhoneNumber;
     */

    public ProductDTO toDto() {
        return ProductDTO.builder()
                .productId(productId)
                .productName(productName)
                .productPrice(productPrice)
                .productStock(productStock)
                .build();
    }
}