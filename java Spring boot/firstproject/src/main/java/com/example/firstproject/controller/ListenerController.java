package com.example.firstproject.controller;

import com.example.firstproject.data.entity.ListenerEntity;
import com.example.firstproject.service.ListenerService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping(value = "Listener")
public class ListenerController {
    @Autowired
    private ListenerService listenerService;

//    public ListenerController(ListenerService listenerService) {
//        this.listenerService = listenerService;
//    }

    @GetMapping
    public String getListener(Long id) {
        listenerService.getEntity(id);
        return "OK";
    }

    @PostMapping
    public void saveListener(String name) {
        ListenerEntity listenerEntity = new ListenerEntity();
        listenerEntity.setName(name);
        listenerService.saveEntity(listenerEntity);
    }

    @PutMapping
    public void updataListener(Long id, String name) {
        ListenerEntity listenerEntity = new ListenerEntity();
        listenerEntity.setId(id);
        listenerEntity.setName(name);
        listenerService.updateEntity(listenerEntity);
    }

    @DeleteMapping
    public void deleteListener(Long id) {
        listenerService.removeEntity(listenerService.getEntity(id));
    }
}
