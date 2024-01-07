package org.example.repository;

import org.example.entity.MemberEntity;
import org.example.entity.ProductEntity;
import org.example.entity.viewEntity.MemberView;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.data.jpa.repository.config.EnableJpaAuditing;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.Objects;

@SpringBootTest
public class JpqlRepositoryTest {
    private MemberRepository memberRepository;
    private ProductRepository productRepository;

    @Autowired
    public JpqlRepositoryTest(@Qualifier("Member") MemberRepository memberRepository, @Qualifier("Product") ProductRepository productRepository) {
        this.memberRepository = memberRepository;
        this.productRepository = productRepository;
    }

//    @BeforeEach // ※주의: 실행 시 CreatedDate가 자동활당되지 않음
    @Test
    void DataInsert() {
        memberRepository.save(new MemberEntity("hero", "임영웅", "서울 은평구 증산동"));
        memberRepository.save(new MemberEntity("iyou", "아이유", "인천 남구 주안동"));
        memberRepository.save(new MemberEntity("jyp", "박진영", "경기 고양시 장항동"));
        memberRepository.save(new MemberEntity("tess", "나훈아", "경기 부천시 중동"));

        productRepository.save(new ProductEntity("삼각김밥", 800, "CJ", 22));
    }

    @Test
    void ViewTest() {
        ViewPrint(memberRepository.findByMemberView());
    }

    @Test
    void View2Test() {
        ViewPrint(memberRepository.findByMemberView2());
    }

    void ViewPrint(List<Object> EntityList) {
        for (Object object : EntityList) {
            System.out.println(object);
        }
    }
}