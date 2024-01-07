package com.example.firstproject.data.dto;

import com.example.firstproject.data.entity.ArticleEntity;
import lombok.*;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
@ToString
public class ArticleDTO {
    private String title;
    private String content;


    public ArticleEntity toEntity() {
        return new ArticleEntity(title, content);
    }
}
