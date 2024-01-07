package com.example.firstproject.service;

import com.example.firstproject.data.entity.ListenerEntity;

public interface ListenerService {
    void saveEntity(ListenerEntity listenerEntity);
    ListenerEntity getEntity(Long id);
    void updateEntity(ListenerEntity listenerEntity);
    void removeEntity(ListenerEntity entity);
}
