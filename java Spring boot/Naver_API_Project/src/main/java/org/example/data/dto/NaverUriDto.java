package org.example.data.dto;

import lombok.*;

@Data
@NoArgsConstructor
@AllArgsConstructor
@ToString
@Builder
public class NaverUriDto {
    private String message;
    private String code;
    private Result result;

    @Getter
    @Setter
    public static class Result {
        private String hash;
        private String orgUrl;
        private String url;
    }
}