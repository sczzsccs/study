package com.example.firstproject.controller;

import com.example.firstproject.data.entity.ProductEntity;
import com.example.firstproject.data.repository.ProductRepository;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.PageRequest;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping(value = "/query")
public class TestqueryContorller {
    private Logger LOGGER = LoggerFactory.getLogger(TestqueryContorller.class);
    private int count = 1;
    @Autowired
    ProductRepository productRepository;

    @GetMapping(value = "/SetData")
    public String SetData() {
        productRepository.save(new ProductEntity(Integer.toString(count), "상품" + count++, 2000* count, 3000* count));
        productRepository.save(new ProductEntity(Integer.toString(count), "상품" + count++, 3000* count, 3000* count));
        productRepository.save(new ProductEntity(Integer.toString(count), "상품" + count++, 1500* count, 200* count));
        productRepository.save(new ProductEntity(Integer.toString(count), "상품" + count++, 4000* count, 5000* count));
        productRepository.save(new ProductEntity(Integer.toString(count), "상품" + count++, 10000* count, 1500* count));
        productRepository.save(new ProductEntity(Integer.toString(count), "상품" + count++, 2000* count, 3000* count));
        productRepository.save(new ProductEntity(Integer.toString(count), "상품" + count++, 3000* count, 3500* count));
        productRepository.save(new ProductEntity(Integer.toString(count), "상품" + count++, 4000* count, 5000* count));
        productRepository.save(new ProductEntity(Integer.toString(count), "상품" + count++, 10000* count, 1500* count));
        productRepository.save(new ProductEntity(Integer.toString(count), "상품" + count++, 2000* count, 4000* count));
        productRepository.save(new ProductEntity(Integer.toString(count), "상품" + count++, 3000* count, 5500* count));
        productRepository.save(new ProductEntity(Integer.toString(count), "상품" + count++, 4000* count, 5000* count));
        productRepository.save(new ProductEntity(Integer.toString(count), "상품" + count++, 10000* count, 1000* count));
        productRepository.save(new ProductEntity(Integer.toString(count), "상품" + count++, 7500* count, 6000* count));
        productRepository.save(new ProductEntity(Integer.toString(count), "상품" + count++, 8000* count, 1700* count));

        return "데이터가 정상적으로 입력되었습니다. <br>입력된 데이터 개수 : "+Integer.toString(count-1);
    }

    @GetMapping(value = "/getPage/{Name}")
    public String GetPage(@PathVariable String Name, Integer PageNum, Integer PageSize) {
        if (PageNum>0) { PageNum--; }
        return Print(productRepository.findByProductNameContainingOrderByProductNameAsc(Name, PageRequest.of(PageNum, PageSize)), PageNum, PageSize);
    }

    @PostMapping(value = "/PostPage")
    public String PostPage(@RequestBody  String Name, Integer PageNum, Integer PageSize) {
        if (PageNum>0) { PageNum--; }
        return Print(productRepository.findByProductNameContaining(Name, PageRequest.of(PageNum, PageSize)), PageNum, PageSize);
    }

    private String Print(List<ProductEntity> found, Integer PageNum, Integer PageSize) {
        StringBuilder EntityList = new StringBuilder();
        LOGGER.info("\n\n### 데이터 Page 단위 출력, 페이지 번호 : {}, 출력되는 데이터 갯수 : {} ###\n", PageNum+1, PageSize);
        for (ProductEntity productEntity : found) {
            LOGGER.info("Print : " + productEntity.toString());
            EntityList.append(productEntity.toString());
            EntityList.append("<br>");
        }
        return EntityList.toString();
    }
}
