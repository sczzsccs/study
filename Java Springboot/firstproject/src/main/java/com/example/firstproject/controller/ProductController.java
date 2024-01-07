package com.example.firstproject.controller;

import com.example.firstproject.common.Contants;
import com.example.firstproject.common.exception.HubException;
import com.example.firstproject.data.dto.ProductDTO;
import com.example.firstproject.service.ProductService;
import jakarta.validation.Valid;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping(value = "/Product")
public class ProductController {
    private final Logger LOGGER = LoggerFactory.getLogger(ProductController.class);
    private final ProductService productService;
    @Autowired
    public ProductController(ProductService productService) {
        this.productService = productService;
    }

    @PostMapping(value = "/Create")
    public ResponseEntity<ProductDTO> Create(@Valid @RequestBody ProductDTO productDTO) {
        // Validation Code Examole
//        if (productDTO.getProductId().equals("") || productDTO.getProductId().isEmpty()) {
//            LOGGER.error("[createProduct] faild Response :: productId is Empty");
//            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(productDTO);
//        }
        ProductDTO response = productService.saveProduct(productDTO);
        LOGGER.info("[CreateProduct] Response :: productId = {}, productName = {}, productPrice = {}, productStock = {}", productDTO.getProductId(), productDTO.getProductName(), productDTO.getProductPrice(), productDTO.getProductStock());
        return ResponseEntity.status(HttpStatus.OK).body(response);
    }

    @GetMapping(value = "/Get/{id}")
    public ProductDTO getDTO(@PathVariable String id) {
        long startTinme = System.currentTimeMillis();
        LOGGER.info("[ProductController] perform {} of API.", "getProduct");

        ProductDTO productDTO = productService.getProduct(id);
        LOGGER.info("[getProduct] Response :: productId = {}, productName = {}, productPrice = {}, productStock = {}, Response Time = {}ms", productDTO.getProductId(), productDTO.getProductName(), productDTO.getProductPrice(), productDTO.getProductStock(), (System.currentTimeMillis()-startTinme));

        return productDTO;
    }

    @PutMapping(value = "/update/{id}")
    public void UpdateDTO(@Valid @RequestBody ProductDTO productDTO) {
        ProductDTO response = productService.saveProduct(productDTO);
        LOGGER.info("[UpdateProduct] Response :: productId = {}, productName = {}, productPrice = {}, productStock = {}", productDTO.getProductId(), productDTO.getProductName(), productDTO.getProductPrice(), productDTO.getProductStock());
    }

    @PutMapping(value = "/delete/{id}")
    public ProductDTO deleteDTO(@PathVariable String id) {
        return null;
    }


    @PostMapping(value = "/exception")
    public void postException() throws HubException {
        throw new HubException(Contants.ExceptionClass.PRODUCT, HttpStatus.FORBIDDEN, "의도한 에러가 발생 접근 금지");
    }

    @GetMapping(value = "/exception")
    public String getException() {
        HubException e = new HubException(Contants.ExceptionClass.PRODUCT, HttpStatus.FORBIDDEN, "</p>의도한 에러가 발생 접근 금지");
        // <h1>Whitelabel Error Page</h1>
        // <div>This application has no explicit mapping for /error, so you are seeing this as a fallback.</p>
        // There was an unexpected error (type=Not Found, status=404).</p>
        // message</div>
        return  "<h1>Whitelabel Error Page</h1>"+
                "<div>This application has no explicit mapping for /error, so you are seeing this as a fallback."+
                "</p>There was an unexpected error (type=" +e.getHttpStatusType()+ ", status=" +Integer.toString(e.getHttpStatusCode())+
                "</p>" +e.getMessage()+"</div>";
    }
}