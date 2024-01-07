package org.example.repository;

import org.example.entity.MemberEntity;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Primary;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.util.List;

@Primary @Qualifier("Member")
public interface MemberRepository extends JpaRepository<MemberEntity, String> {
    @Query("select v from MemberView v")
    List<Object> findByMemberView();
    @Query("select v from MemberView2 v")
    List<Object> findByMemberView2();
}