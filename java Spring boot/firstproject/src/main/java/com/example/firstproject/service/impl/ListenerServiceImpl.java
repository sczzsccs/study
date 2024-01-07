package com.example.firstproject.service.impl;

import com.example.firstproject.data.entity.ListenerEntity;
import com.example.firstproject.data.repository.ListenerRepository;
import com.example.firstproject.service.ListenerService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class ListenerServiceImpl implements ListenerService {
    private final ListenerRepository listenerRepository;
    @Autowired
    public ListenerServiceImpl(ListenerRepository listenerRepository) {
        this.listenerRepository = listenerRepository;
    }

    @Override
    public void saveEntity(ListenerEntity listenerEntity) {
        listenerRepository.save(listenerEntity);
    }
    @Override
    public ListenerEntity getEntity(Long id) {
        return listenerRepository.findById(id).get();
    }
    @Override
    public void updateEntity(ListenerEntity listenerEntity) {
        listenerRepository.save(listenerEntity);
    }
    @Override
    public void removeEntity(ListenerEntity listenerEntity) {
        listenerRepository.delete(listenerEntity);
    }
}
