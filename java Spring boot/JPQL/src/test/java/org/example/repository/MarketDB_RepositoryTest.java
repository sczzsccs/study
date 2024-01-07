package org.example.repository;

import org.example.entity.Buy;
import org.example.entity.GirlMember;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDate;
import java.util.List;

@SpringBootTest
public class MarketDB_RepositoryTest {
    private final BuyRepository buyRepository;
    private final GirlMemberRepository girlMemberRepository;

    @Autowired
    public MarketDB_RepositoryTest(
            @Qualifier("Buy") BuyRepository buyRepository,
            @Qualifier("Girl") GirlMemberRepository girlMemberRepository) {
        this.buyRepository = buyRepository;
        this.girlMemberRepository = girlMemberRepository;
    }

//    @Test @Transactional
    @BeforeEach
    void DataInsert() {
        buyRepository.save(new Buy(null, "BLK", "지갑", null, 30, 2));
        buyRepository.save(new Buy(null, "BLK", "맥북프로", "디지털", 1000, 1));
        buyRepository.save(new Buy(null, "APN", "아이폰", "디지털", 200, 1));
        buyRepository.save(new Buy(null, "MMU", "아이폰", "디지털", 200, 5));
        buyRepository.save(new Buy(null, "BLK", "청바지", "패션", 50, 3));
        buyRepository.save(new Buy(null, "MMU", "에어팟", "디지털", 80, 10));
        buyRepository.save(new Buy(null, "GRL", "혼공SQL", "서적", 15, 5));
        buyRepository.save(new Buy(null, "APN", "혼공SQL", "서적", 15, 2));
        buyRepository.save(new Buy(null, "APN", "청바지", "패션", 50, 1));
        buyRepository.save(new Buy(null, "MMU", "지갑", null, 30, 1));
        buyRepository.save(new Buy(null, "APN", "혼공SQL", "서적", 15, 1));
        buyRepository.save(new Buy(null, "MMU", "지갑", null, 30, 4));

        girlMemberRepository.save(new GirlMember("TWC", "트와이스", 9, "서울", "02",
                "1111-1111", 167, LocalDate.of(2015, 10, 19)));
        girlMemberRepository.save(new GirlMember("BLK", "블랙핑크", 4, "경남", "055",
                "2222-2222", 163, LocalDate.of(2016,8,8)));
        girlMemberRepository.save(new GirlMember("WMN", "여자친구", 6, "경기", "031",
                "3333-3333", 166, LocalDate.of(2015,1,15)));
        girlMemberRepository.save(new GirlMember("OMY", "오마이걸", 7, "서울", null,
                null, 160, LocalDate.of(2015,4,21)));
        girlMemberRepository.save(new GirlMember("GRL", "소녀시대", 8, "서울", "02",
                "4444-4444", 168, LocalDate.of(2007,8,2)));
        girlMemberRepository.save(new GirlMember("ITZ", "잇지", 5, "경남", null,
                null, 167, LocalDate.of(2019, 2, 12)));
        girlMemberRepository.save(new GirlMember("RED", "레드벨벳", 4, "경북", "054",
                "5555-5555", 161, LocalDate.of(2014,8,1)));
        girlMemberRepository.save(new GirlMember("APN", "에이핑크", 6, "경기", "031",
                "7777-7777", 164, LocalDate.of(2011,2,10)));
        girlMemberRepository.save(new GirlMember("SPC", "우주소녀", 13, "서울", "02",
                "8888-8888", 162, LocalDate.of(2016,2,25)));
        girlMemberRepository.save(new GirlMember("MMU", "마마무", 4, "전남", "061",
                "9999-9999", 165, LocalDate.of(2014,6,19)));
    }

    @Test
    void Datafind() {
        System.out.println("\n\n==== Buy Data ====");
        findPrint(buyRepository.findBuyAll());

        System.out.println("\n\n==== Girl Member Data ====");
        findPrint(girlMemberRepository.findAllGirl());
    }

    @Test
    void DatafindNameTest() {
//        findPrint(girlMemberRepository.findByName("블랙핑크"));
        List<Object> result = girlMemberRepository.addr_height_debutDate_findByName("블랙핑크");

        StringBuilder printBuff = new StringBuilder();
        for (Object row : result) {
            for (Object object : (Object[]) row) {
                printBuff.append(object).append("\n");
            }
        }
        System.out.println("\n\n==== find Girl Member N  ame: 블랙핑크 ====\n"+printBuff);
    }

    void findPrint(List<Object> Entities) {
        for (Object object: Entities) {
            System.out.println(object);
        }
    }
}