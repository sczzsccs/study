package org.example.repository;

import org.example.entity.Buy;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Primary;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.util.List;

@Primary @Qualifier("Buy")
public interface BuyRepository extends JpaRepository<Buy, Integer> {
    @Query("select b from Buy b")
    List<Object> findBuyAll();
}