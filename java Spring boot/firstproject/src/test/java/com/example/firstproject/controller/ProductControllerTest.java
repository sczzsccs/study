package com.example.firstproject.controller;

import com.example.firstproject.data.dto.ProductDTO;
import com.example.firstproject.service.impl.ProductServiceImpl;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.google.gson.Gson;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;

import static org.mockito.BDDMockito.given;
import static org.mockito.Mockito.verify;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultHandlers.print;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@WebMvcTest(ProductController.class)
// @AutoConfigureWebMvc // 이 어노테이션을 통해 MockMvc를 Builder 없이 주입받을 수 있음
class ProductControllerTest {
    @Autowired
    private MockMvc mockMvc;

    @MockBean // ProductController에서 잡고 있는 Bean 객체에 대해 Mock형태의 객체를 생성해줌
    ProductServiceImpl productService;

    // http://localhost:8080/product/get/{id}
    @Test @DisplayName(value = "Product 데이터 가져오기 테스트")
    void getDTOTest() throws Exception {
        String id = "12315";

        // given: Mock 객체가 특정 상황에서 해야하는 행위를 정의하는 메소드
        given(productService.getProduct(id)).willReturn(
                new ProductDTO("15871", "pen", 5000, 2000));

        // andExpect : 기대하는 값이 나왔는지 체크해볼 수 있는 메소드
        mockMvc.perform(get("/Product/Get/"+id) // uri
                                .contentType(MediaType.APPLICATION_JSON)) // contentType 설정
                .andExpect(status().isOk())
                .andExpect(jsonPath("productId").exists())
                .andExpect(jsonPath("productName").exists())
                .andExpect(jsonPath("productPrice").exists())
                .andExpect(jsonPath("productStock").exists())
                .andDo(print());
        // verify : 해당 객체의 메소드가 실행되었는지 체크해줌
        verify(productService).getProduct(id);
    }

    @Test @DisplayName("Product 데이터 생성 테스트")
    void createTest() throws Exception {
        // Mock 객체에서 특정 메소드가 실행되는 경우 실제 Return을 줄 수 없기 때문에 아래와 같이 가정 사항을 만들어줌
//        ProductDTO productDTO = new ProductDTO("15871", "pen", 5000, 2000);
        given(productService.saveProduct(
                new ProductDTO("15871", "pen", 5000, 2000)))
                .willReturn(new ProductDTO("15871", "pen", 5000, 2000));

        ProductDTO productDTO = ProductDTO.builder().productId("15871").productName("pen").productPrice(5000).productStock(2000).build();
        Gson gson = new Gson();
        String content = gson.toJson(productDTO);

        // 아래 코드로 json 형태 변경 작업을 대체할 수 있음
        String json = new ObjectMapper().writeValueAsString(productDTO);

        mockMvc.perform(post("/Product/Create")
                        .content(content)
                        .contentType(MediaType.APPLICATION_JSON))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.productId").exists()) // json path의 depth가 깊어지면 .을 추가
                .andExpect(jsonPath("$.productName").exists())
                .andExpect(jsonPath("$.productPrice").exists())
                .andExpect(jsonPath("$.productStock").exists())
                .andDo(print());
        verify(productService).saveProduct(productDTO);
    }
}