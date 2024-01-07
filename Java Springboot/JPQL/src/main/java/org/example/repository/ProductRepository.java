package org.example.repository;

import org.example.entity.ProductEntity;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.data.jpa.repository.JpaRepository;

@Qualifier("Product")
public interface ProductRepository extends JpaRepository<ProductEntity, String> {
}