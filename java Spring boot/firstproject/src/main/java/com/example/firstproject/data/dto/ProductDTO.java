package com.example.firstproject.data.dto;

import com.example.firstproject.data.entity.ProductEntity;
import jakarta.validation.constraints.Max;
import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotNull;
import lombok.*;

@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class ProductDTO {

    @NotNull
    // @Size(min = 8, max = 8) // char[8]
    private String productId;

    @NotNull
    private String productName;

    @NotNull
    @Min(value = 500) @Max(value = 3000000)
    private int productPrice;

    @NotNull
    @Min(value = 0) @Max(value = 9999)
    private int productStock;

    public ProductEntity toEntity() {
        return ProductEntity.builder()
                .productId(productId)
                .productName(productName)
                .productPrice(productPrice)
                .productStock(productStock)
                .build();
    }
}