package org.example.repository;

import org.example.entity.GirlMember;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import java.util.List;

@Qualifier("Girl")
public interface GirlMemberRepository extends JpaRepository<GirlMember, String> {
    @Query("select G from GirlMember G")
    List<Object> findAllGirl();

    @Query("select g from GirlMember g where g.name like :name")
    List<Object> findByName(String name);

    @Query("select g.addr, g.height, g.debutDate from GirlMember g where g.name like :name")
    List<Object> addr_height_debutDate_findByName(String name);
}