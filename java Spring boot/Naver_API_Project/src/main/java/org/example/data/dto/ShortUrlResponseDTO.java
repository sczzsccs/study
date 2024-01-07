package org.example.data.dto;

import lombok.*;

@Getter
@Setter
@ToString
@AllArgsConstructor
@NoArgsConstructor
public class ShortUrlResponseDTO {
    private String OriginalUrl;
    private String ShortUrl;
}
