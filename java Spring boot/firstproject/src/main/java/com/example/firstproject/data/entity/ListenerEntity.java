package com.example.firstproject.data.entity;

import com.example.firstproject.data.entity.listener.CustomListener;
import jakarta.persistence.*;
import lombok.*;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Entity
@Builder
@ToString
@Table(name = "listener")
@EntityListeners(CustomListener.class)
public class ListenerEntity extends BaseEntity {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;
}