package com.example.firstproject.data.entity;

import com.example.firstproject.data.dto.ArticleDTO;
import jakarta.persistence.*;
import lombok.*;

@Entity // DB가 해당 객체를 인식 가능
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
@Table(name = "article_table")
public class ArticleEntity {
    @Id // 대표값을 지정
    @GeneratedValue // 자동생성 Value
    private long Id; // PK(기본 키)
    @Column
    private String Title;
    @Column
    private String Content;

    public ArticleEntity(String Title, String Content) {
        this.setTitle(Title);
        this.setContent(Content);
    }

    public ArticleDTO toDto() {
        return ArticleDTO.builder()
                .title(Title)
                .content(Content)
                .build();
    }

    public String toString() {
        return "ArticleEntity(Id=" + this.getId() + ", Title=" + this.getTitle() + ", Content=" + this.getContent() + ")";
    }
}