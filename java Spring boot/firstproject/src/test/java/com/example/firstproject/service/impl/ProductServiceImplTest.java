package com.example.firstproject.service.impl;

import com.example.firstproject.data.dto.ProductDTO;
import com.example.firstproject.data.handler.ProductDataHandler;
import com.example.firstproject.data.handler.impl.ProductDataHandlerImpl;
import com.example.firstproject.service.ProductService;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mockito;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.context.annotation.Import;
import org.springframework.test.context.junit.jupiter.SpringExtension;

import static org.mockito.Mockito.verify;

//@SpringBootTest(classes = {ProductDataHandlerImpl.class, ProductServiceImpl.class})
@ExtendWith(SpringExtension.class)
@Import({ProductDataHandlerImpl.class, ProductServiceImpl.class})
public class ProductServiceImplTest {
    @MockBean
    private ProductDataHandler productDataHandler;

    @Autowired
    private ProductService productService;

    private final ProductDTO DTOtestVal = new ProductDTO("1231", "1231", 2000, 3000);
    private ProductDTO productDTOtest;

    @Test
    void saveProductTest() {
        Mockito.when(productDataHandler.saveProductEntity(DTOtestVal))
                .thenReturn(DTOtestVal.toEntity());

        productDTOtest = productService.saveProduct(DTOtestVal);
        Assertions.assertEquals(productDTOtest.getProductId(), DTOtestVal.getProductId());
        Assertions.assertEquals(productDTOtest.getProductName(), DTOtestVal.getProductName());
        Assertions.assertEquals(productDTOtest.getProductPrice(), DTOtestVal.getProductPrice());
        Assertions.assertEquals(productDTOtest.getProductStock(), DTOtestVal.getProductStock());

        verify(productDataHandler).saveProductEntity(DTOtestVal);
        System.out.println(
                "saveProductTest : \n"+
                productDTOtest.toString());
    }

    @Test @DisplayName("Product GetData Test")
    void getProductTest() {
        // given
        Mockito.when(
                productDataHandler.getProductEntity(DTOtestVal.getProductId()))
                .thenReturn(DTOtestVal.toEntity());

        productDTOtest = productService.getProduct(DTOtestVal.getProductId());
        Assertions.assertEquals(productDTOtest.getProductId(), DTOtestVal.getProductId());
        Assertions.assertEquals(productDTOtest.getProductName(), DTOtestVal.getProductName());
        Assertions.assertEquals(productDTOtest.getProductPrice(), DTOtestVal.getProductPrice());
        Assertions.assertEquals(productDTOtest.getProductStock(), DTOtestVal.getProductStock());

        verify(productDataHandler).getProductEntity(DTOtestVal.getProductId());
        System.out.println(
                "getProductTest : \n"+
                        productDTOtest.toString());
    }
}